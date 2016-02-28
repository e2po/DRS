//'use strict';
//
//angular.module('drsApp')
//    .config(['$routeProvider', function($routeProvider) {
//        $routeProvider
//            .when('/cloning', {
//                //controller: 'PartitionPickerApp.PartitionPickerCtrl',
//                //module: 'PartitionPickerApp',
//                controller: 'PartitionPickerApp.PartitionPickerCtrl',
//                templateUrl: 'partition-picker/views/select_partitions.html'
//            })
//            .when('/choose_partitions', {
//                action: 'PartitionPickerApp.PartitionPickerCtrl',
//                templateUrl: 'views/select_partitions.html'
//            })
//            .when('/test', {
//                action: 'PartitionPicker.PartitionPickerCtrl',
//                templateUrl: 'index.html'
//            })
//            .otherwise({
//                redirectTo: '/cloning'
//            });
//    }]);