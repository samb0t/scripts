// ==UserScript==
// @name         Keep owa alive
// @namespace    http://
// @version      0.1
// @description  keeps the outlook web access page cookie alive
// @author       sambot
// @match        https://*/owa/
// @require		 https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.7.0/underscore-min.js
// @grant        none
// ==/UserScript==

var timeoutHandle;
setReloadTimeout();
window.onclick = function() { lazyTimeoutReset(); }
window.onkeypress = function() { lazyTimeoutReset(); }
var lazyTimeoutReset = _.debounce(resetTimeout, 1000, true);

function resetTimeout() {
    if (timeoutHandle) {
    	window.clearTimeout(timeoutHandle);
        setReloadTimeout();
    }
}

function setReloadTimeout() {
	 timeoutHandle = window.setTimeout(function() { location.reload(); }, 120000);  
}