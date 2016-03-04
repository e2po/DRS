/*
"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       March 24th, 2016
"""
*/
(function(app){
    var mftAnalyserController = function($scope, mySocket){
        $scope.deletedRecords = [];
        $scope.progress = 0;
        $scope.partitions = [];
        $scope.analysisCompleted = false;

        $scope.getPartitions = function() {
            console.log('requesting list of available partitions...');
            mySocket.emit('request:partitions');
        };

        $scope.analyseMft = function() {
            console.log('requesting mft analysis...');

            $scope.analysisCompleted = false;
            $scope.deletedRecords = [];
            $scope.progress = 0;
            mySocket.emit('request:mft_analyse', $scope.sourcePath);
        };

        mySocket.on('response:partitions', function(data) {
            $scope.partitions = JSON.parse(data);
        });

        mySocket.on('deleted_file_found', function(data) {
            $scope.analysisCompleted = true;
            console.log('mft analysis completed.');
            $scope.deletedRecords = JSON.parse(data);
        });

        mySocket.on('mft_analyser_progress', function(data) {
            var current = data['current'];
            var total = data['total'];
            $scope.progress = current/total * 100;
        });
    };

    app.controller("mftAnalyserController", ["$scope", "mySocket", mftAnalyserController]);
}(angular.module("drsApp")));