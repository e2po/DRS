(function(){
    'use strict';

    angular.module('drsApp', [
        'ui.router',
        'ngMaterial',
        'ngAnimate',
        'btford.socket-io'
    ]).config([
        '$stateProvider',
        '$urlRouterProvider',
        function($stateProvider, $urlRouterProvider) {
            $urlRouterProvider.otherwise('/');

            $stateProvider
                .state("partitionPicker", {
                    url: "/picker",
                    templateUrl: "drsApp/partitionPicker/partition-picker.html",
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
                    templateUrl: "drsApp/mftAnalysis/mftAnalysis.html",
                    controller: "mftAnalysisController",
                    controllerAs: "ctrl"
                })
        }]);
})();