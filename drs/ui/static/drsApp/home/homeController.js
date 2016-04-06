/*
"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""
 */
(function(app){
    var homeController = function($scope){
        $scope.number = 2+2;
    };

    app.controller("homeController", ["$scope", homeController]);
}(angular.module("drsApp")));