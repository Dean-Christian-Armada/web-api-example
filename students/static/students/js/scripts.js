var domainName = window.location.href;
var domainName = domainName.split("/");
var domainName = domainName[0] + "//" + domainName[2];

// START modules
var StudentListSystem = angular.module('StudentListSystem', ['ngRoute']);
// END modules

// START configurations
	StudentListSystem.config(function($interpolateProvider){
		$interpolateProvider.startSymbol('[[');
		$interpolateProvider.endSymbol(']]');
	});
	// START Included to by pass the Django CSRF
		StudentListSystem.config(function($httpProvider){
			$httpProvider.defaults.xsrfCookieName = 'csrftoken';
			$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
		});
	// END Included to by pass the Django CSRF
	StudentListSystem.config(function($routeProvider){
		$routeProvider
		// Route for the homepage
		.when('/', {
			title: 'Home',
			templateUrl: '/static/students/html/home.html',
			controller: 'MainController'
		})
		// Route for the student form page
		.when('/form', {
			title: 'Form',
			templateUrl: '/static/students/html/form.html',
			controller: 'FormController'
		})
		// Route for the section form page
		.when('/form/section', {
			title: 'Section Form',
			templateUrl: '/static/students/html/section-form.html',
			controller: 'SectionFormController'
		})
		// Route for the profile page
		.when('/list/profile', {
			title: 'Profile',
			templateUrl: '/static/students/html/profile.html',
			controller: 'ProfileController'
		})
		// Route for the students list page
		.when('/list', {
			title: 'Student List',
			templateUrl: '/static/students/html/list.html',
			controller: 'ListController'
		});
	})
	// START dynamic title
		.run(function($rootScope){
			$rootScope.$on("$routeChangeSuccess", function (event, currentRoute, previousRoute) {
		    document.title = currentRoute.title;
		  });
		});
	// END dynamic title
// END Configurations

// START Controllers
StudentListSystem.controller('MainController', function($scope){
	$scope.title = "Home";
});
StudentListSystem.controller('AboutController', function($scope){
	$scope.title = "Profile";
});
StudentListSystem.controller('FormController', function($scope){
	$scope.title = "Form";
});
StudentListSystem.controller('SectionFormController', function($scope, $http){
	$scope.title = "Section Formsss";
	$scope.SelectedFruit = { edit:false };
	$http.get(domainName+'/api/v1/section/')
	.then(function(response){
		// alert(JSON.stringify(response.data));
		$scope.Sections = response.data;
		$scope.Sections.forEach(function(x){
			x.edit = false;
		});
	});
	$scope.ajax_request = function(section_name){
		// alert('dean');
		// alert(section_name['name']);
		$http.post(domainName+'/api/v1/section/', section_name)
		.then(function(response){
			// Handles success
			// alert('Data Added');
			// alert(JSON.stringify(response));
			$scope.Notifications = true;
			$scope.Success = response.data;
			$http.get(domainName+'/api/v1/section/')
			.then(function(response){
				$scope.Sections = response.data;
			});
			$scope.section_name = "";
			angular.element(document.querySelector('.error')).text("Form Submitted");
		}, function(response){
			// Handles errors
			$scope.Notifications = true;
			$scope.Errors = response.data;
			// alert('Data Error');
			// alert(JSON.stringify(response));
		});
	};
	$scope.ajax_delete = function(id){
		// alert(id);
		$http.delete(domainName+'/api/v1/section/'+id)
		.then(function(response){
			$scope.Notifications = true;
			$scope.Deleted = response.data;
			// alert(JSON.stringify(response));
			$http.get(domainName+'/api/v1/section/')
			.then(function(response){
				$scope.Sections = response.data;
			});
		}, function(response){
			$scope.Notifications = true;
			$scope.Errors = response.data;
		});
	}
	$scope.ajax_update_button = function(object){
		object.edit = !object.edit;
	}
	$scope.ajax_update = function(section){
		$http.put(domainName+'/api/v1/section/'+section.id, section)
		.then(function(response){
			$scope.Notifications = true;
			$scope.Updated = response.data;
			$http.get(domainName+'/api/v1/section/')
			.then(function(response){
				$scope.Sections = response.data;
			});
		}, function(response){
			$scope.Notifications = true;
			$scope.Errors = response.data;
		});
		// alert(id);
		// alert(name);
		// alert(JSON.stringify(section));
	}
});
StudentListSystem.controller('ListController', function($scope){
	$scope.title = "List";
});
StudentListSystem.controller('ssectionFormController', function($scope){
});
// END Controllers