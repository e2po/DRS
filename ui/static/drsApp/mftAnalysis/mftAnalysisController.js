(function(app){
    var mftAnalysisController = function($scope){
        $scope.number = 2+2;
    };

    app.controller("mftAnalysisController", ["$scope", mftAnalysisController]);
}(angular.module("drsApp")));