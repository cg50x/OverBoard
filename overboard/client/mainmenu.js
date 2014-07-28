Template.mainMenu.events({
    'click #logout' : function(e, t) {
        Meteor.logout(function(err) {
            if (err) {
                alert("Couldn't log you out!");
            } else {
                Router.go('frontpage');
            }
        });
    }
});

Template.mainMenu.rendered = function() {
    setInterval(function() {
        $('h1').toggle();
    }, 1000);
};