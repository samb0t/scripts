// ==UserScript==
// @name       TrelloBigger
// @version    0.1
// @description  this is awful, but wanted to test a commit
// @match      https://trello.com/card/*
// @copyright  2013+, sambot
// @require http://code.jquery.com/jquery-latest.js
// ==/UserScript==

$(function () {
    setTimeout(function () {
        var width = $(window).width();
		
        $(".window").css({width: width-100, left: '50px'}); 
        $(".window-main-col").css({width: width-500});
    }, 500);
});

