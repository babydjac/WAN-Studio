import { app } from "../../scripts/app.js";

const MODE_COLORS = {
    SFW: { color: "#2563eb", bgcolor: "#0f172a" },
    NSFW: { color: "#dc2626", bgcolor: "#450a0a" },
};

function applyModeColor(node, mode) {
    const palette = MODE_COLORS[mode] || MODE_COLORS.SFW;
    node.color = palette.color;
    node.bgcolor = palette.bgcolor;
    node.setDirtyCanvas?.(true, true);
}

function getCurrentMode(node) {
    const widget = node.widgets?.find((w) => w.name === "content_mode");
    return widget?.value || "SFW";
}

app.registerExtension({
    name: "WAN22PromptStudio.ui",
    
    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== "WAN22PromptStudioNode") return;

        // Override onNodeCreated
        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            const result = onNodeCreated?.apply(this, arguments);
            this.serialize_widgets = true;
            
            // Apply initial color
            const mode = getCurrentMode(this);
            applyModeColor(this, mode);
            
            return result;
        };

        // Override onConfigure (for loaded workflows)
        const onConfigure = nodeType.prototype.onConfigure;
        nodeType.prototype.onConfigure = function () {
            const result = onConfigure?.apply(this, arguments);
            
            // Apply color after configuration
            setTimeout(() => {
                const mode = getCurrentMode(this);
                applyModeColor(this, mode);
            }, 10);
            
            return result;
        };

        // Override onDrawBackground to constantly check and apply colors
        const onDrawBackground = nodeType.prototype.onDrawBackground;
        nodeType.prototype.onDrawBackground = function (ctx) {
            const result = onDrawBackground?.apply(this, arguments);
            
            // Check current mode and ensure colors are correct
            const currentMode = getCurrentMode(this);
            const expectedPalette = MODE_COLORS[currentMode];
            
            // If colors don't match, reapply
            if (this.color !== expectedPalette.color || this.bgcolor !== expectedPalette.bgcolor) {
                applyModeColor(this, currentMode);
            }
            
            return result;
        };
        
        // Hook widget value changes
        const onExecutionStart = nodeType.prototype.onExecutionStart;
        nodeType.prototype.onExecutionStart = function () {
            const result = onExecutionStart?.apply(this, arguments);
            
            // Ensure colors are correct before execution
            const mode = getCurrentMode(this);
            applyModeColor(this, mode);
            
            return result;
        };
    },
});