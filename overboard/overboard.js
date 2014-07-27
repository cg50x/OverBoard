if(Meteor.isClient) {
    Template.login.events({
        'submit #login-form' : function(e, t) {
            e.preventDefault();
            var email = t.find('#login-email').value,
                password = t.find('#login-password').value;
            // DO validation here
            Meteor.loginWithPassword(email, password, function(err) {
                if(err) {
                    alert('User not found!');
                } else {
                    alert('User FOUND!');
                }
            });
            return false;
        }
    });

    Template.register.events({
        'submit #register-form' : function(e, t) {
            e.preventDefault();
            var email = t.find('#account-email').value,
                password = t.find('#account-password').value;
            // DO validation here
            Accounts.createUser({email: email, password: password}, function(err) {
                if (err) {
                    alert('Sorry! Could not create the user');
                } else {
                    alert('User created!');
                }
            });
            return false;
        }
    });
}