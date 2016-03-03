(function(app){
    var homeController = function($scope){
        $scope.number = 2+2;
    };

    app.controller("homeController", ["$scope", homeController]);
}(angular.module("drsApp")));