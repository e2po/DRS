(function(){
    'use strict';

    angular.module('drsApp', [
        'ui.router',
        'ngMaterial',
        'ngAnimate',
        'btford.socket-io',
        'partitionPicker'
    ]).config([
        '$stateProvider',
        '$urlRouterProvider',
        function($stateProvider, $urlRouterProvider) {
            $urlRouterProvider.otherwise('/');

            $stateProvider
                .state("partitionPicker", {
                    url: "/partitionPicker",
                    templateUrl: "drsApp/partitionPicker/partition-picker.html",
                    controller: "partitionPickerController",
                    controllerAs: "ctrl"
                })
        }]);
})();



//'use strict';
//
//angular.module('drsApp', [
//        'ngMaterial',
//        'ngAnimate',
//        'btford.socket-io',
//
//        'ngRoute',
//        'drsApp.partition-picker'
//    ])
//    .config(function ($routeProvider) {
//        $routeProvider
//            .when('/', {
//                templateUrl: 'partition-picker/partition-picker.html',
//                controller: 'homeController',
//                controllerAs: 'ctrl'
//
//            })
//            .otherwise({
//                redirectTo: '/'
//            });
//    });

//// Define all modules with no dependencies
//angular.module('PartitionPickerApp', []);
//angular.module('PartitionClonerApp', []);
//
//// Lastly, define 'main' module and inject other modules as dependencies
//angular.module('drsApp',
//    [
//        'ngMaterial',
//        'ngAnimate',
//        'btford.socket-io',
//        'ngRoute',
//        'PartitionPickerApp',
//        'PartitionClonerApp'
//    ]);
//
////angular.module('drsApp', ['ngMaterial', 'ngAnimate', 'btford.socket-io', 'ngRoute'])
////    .config(['$routeProvider', function($routeProvider) {
////        'use strict';
////        $routeProvider
////            .when('/cloning', {
////                controller: 'CloneCtrl',
////                templateUrl: 'views/select_partitions.html'
////            })
////            .when('/choose_partitions', {
////                controller: 'CloneCtrl',
////                templateUrl: 'views/select_partitions.html'
////            })
////            .when('/test', {
////                controller: 'CloneCtrl',
////                templateUrl: 'index.html'
////            })
////            .otherwise({
////                redirectTo: '/cloning'
////            });
////    }]);
