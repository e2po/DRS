(function(app){
    var partitionPickerController = function($scope){
        $scope.number = 2+2;
    };

    app.controller("partitionPickerController", ["$scope", partitionPickerController]);
}(angular.module("drsApp")));