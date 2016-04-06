/*
"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""
*/
(function(){
    'use strict';

    angular.module('drsApp', [
        'ui.router',
        'ngMaterial',
        'ngAnimate',
        'btford.socket-io'
    ])
    .config([
        '$stateProvider',
        '$urlRouterProvider',
        function($stateProvider, $urlRouterProvider) {
            $urlRouterProvider.otherwise('/mft');

            $stateProvider
                .state("partitionPicker", {
                    url: "/picker",
                    templateUrl: "drsApp/partitionPicker/partitionPicker.html",
                    controller: "partitionPickerController",
                    controllerAs: "ctrl"
                })
                .state("home", {
                    url: "/",
                    templateUrl: "drsApp/home/home.html",
                    controller: "homeController",
                    controllerAs: "ctrl"
                })
                .state("mftAnalysis", {
                    url: "/mft",
                    templateUrl: "drsApp/mftAnalyser/mftAnalyser.html",
                    controller: "mftAnalyserController",
                    controllerAs: "ctrl"
                })
        }])
    .factory('mySocket', function (socketFactory) {
        var mySocket = socketFactory({
            ioSocket: io.connect()
        });
        mySocket.forward('error');
        return mySocket;
    })
})();
