(function () {
    'use strict';

    var controllerId = 'customers.picker.ctrl';

    /**
     * Purpose: show details of a specific customer
     */
    angular.module('eepdev.partition-picker.controllers').controller(controllerId, ['$scope', '$routeParams', 'partitionService', controllerFunc]);

    function controllerFunc($scope, $routeParams, partitionService)
    {
        $scope.partitions = partitionService.getPartitions();
    }
})();
//angular.module('PartitionPickerApp')
//    .controller('PartitionPickerCtrl', function($scope, socket, $location) {
//        $scope.partitions = [];
//        $scope.selectedSource = '';
//        $scope.selectedDestination = '';
//
//        $scope.startCloning = function() {
//            $location.url('/test');
//        };
//
//        $scope.getPartitions = function() {
//            console.log('sending request to server');
//            socket.emit('request:partitions');
//        };
//
//        socket.on('response:partitions', function(data) {
//            var obj = JSON.parse(data);
//            console.log(obj[1].path);
//
//            $scope.partitions = obj;
//        });
//    });