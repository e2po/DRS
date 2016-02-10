/**
 * Created by elvis on 07/02/16.
 */
var app = angular.module("app", []);

//var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

app.controller("AppCtrl", function () {
    var app = this;

    app.message = "Hello";
});
