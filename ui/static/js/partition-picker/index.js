angular.module('eepdev.partition-picker',
        [
            'eepdev.partition-picker.controllers',
            'eepdev.partition-picker.services'
        ])
    .config(function ($routeProvider) {
    $routeProvider
        .when('/picker', {
            templateUrl: 'js/partition-picker/views/select_partitions.html',
            controller: 'picker.ctrl'
        });
});