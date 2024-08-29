"use strict";
window.addEventListener("DOMContentLoaded", () => {
    const tabbar = new TabBar("nav");
});
class TabBar {
    
    constructor(el) {
        var _a, _b;
        this.el = document.querySelector(el);
        (_a = this.el) === null || _a === void 0 ? void 0 : _a.setAttribute("data-pristine", "true");
        (_b = this.el) === null || _b === void 0 ? void 0 : _b.addEventListener("click", this.switchTab.bind(this));
    }
    
    switchTab(e) {
        var _a, _b;
        
        (_a = this.el) === null || _a === void 0 ? void 0 : _a.removeAttribute("data-pristine");
        const target = e.target;
        const href = target.getAttribute("href");
        
        if (href) {
            
            const currentPage = (_b = this.el) === null || _b === void 0 ? void 0 : _b.querySelector(`[aria-current="page"]`);
            if (currentPage) {
                currentPage.ariaCurrent = null;
            }
            
            target.ariaCurrent = "page";
        }
    }
}