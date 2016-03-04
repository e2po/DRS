/*
"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       March 24th, 2016
"""
* */
(function(app){
    var partitionPickerController = function($scope, mySocket){
        $scope.number = 2+3;
        $scope.partitions = [1,2,3];

        $scope.getPartitions = function() {
            console.log('sending request to server');
            mySocket.emit('request:partitions');
        };

        mySocket.on('response:partitions', function(data) {
            var obj = JSON.parse(data);
            console.log(obj);

            for (var i=0; i<obj.length; i++) {
                console.log(obj[i]);
            }
            console.log($scope.partitions);
            $scope.partitions = obj;
            console.log($scope.partitions[0].path);
        });

        $scope.getPartitions();

    };

    app.controller("partitionPickerController", ["$scope", "mySocket", partitionPickerController]);
}(angular.module("drsApp")));