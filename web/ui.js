import { app } from "../../scripts/app.js";

const MODE_COLORS = {
  SFW: { color: "#2563eb", bgcolor: "#0f172a" },
  NSFW: { color: "#dc2626", bgcolor: "#450a0a" },
};

function chainCallback(object, property, callback) {
  if (!object) {
    console.warn("WAN22PromptStudio: missing object for", property);
    return;
  }
  const prev = object[property];
  if (prev) {
    object[property] = function (...args) {
      const result = prev.apply(this, args);
      callback.apply(this, args);
      return result;
    };
  } else {
    object[property] = callback;
  }
}

function applyModeColor(node, mode) {
  const palette = MODE_COLORS[mode] || MODE_COLORS.SFW;
  node.color = palette.color;
  node.bgcolor = palette.bgcolor;
  node.setDirtyCanvas?.(true, true);
}

function hookModeWidget(node) {
  if (node.__wan22ModeHooked) {
    const widget = node.widgets?.find((w) => w.name === "content_mode");
    applyModeColor(node, widget?.value || "SFW");
    return;
  }
  const widget = node.widgets?.find((w) => w.name === "content_mode");
  if (!widget) {
    applyModeColor(node, "SFW");
    return;
  }
  node.__wan22ModeHooked = true;
  const syncColor = () => applyModeColor(node, widget.value);
  const original = widget.callback;
  widget.callback = (value) => {
    syncColor();
    original?.call(widget, value);
  };
  syncColor();
}

app.registerExtension({
  name: "WAN22PromptStudio.ui",
  async beforeRegisterNodeDef(nodeType, nodeData) {
    if (nodeData.name !== "WAN22PromptStudioNode") return;

    chainCallback(nodeType.prototype, "onNodeCreated", function () {
      this.serialize_widgets = true;
      hookModeWidget(this);
    });

    chainCallback(nodeType.prototype, "onConfigure", function () {
      hookModeWidget(this);
    });
  },
});
