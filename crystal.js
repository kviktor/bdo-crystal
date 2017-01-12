var app = angular.module('app', []);

function inString(a, b) {
  return a.toLowerCase().indexOf(b.toLowerCase()) > -1;
}

app.controller('crystalController', function($scope, $http) {
  $http.get('/misc/crystals.json').then(function(res) {
    $scope.crystals = res.data;
  });

  $scope.sockets = ["All", "Weapon", "Secondary", "Gloves", "Shoes", "Helmet", "Armor", "Any"];
  $scope.rarities = ["All", "Green", "Blue", "Yellow", "Orange"];

  $scope.show = function(item) {
    if($scope.socket != "All" && $scope.socket != item.slot) return false;
    if($scope.rarity != "All" && $scope.rarity != item.rarity) return false;
    return inString(item.name, $scope.filter) || inString(item.effect, $scope.filter);
  };
});
