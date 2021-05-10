# FlaskNew

In this exercise will update your web site (old Flask) to include a password update form and provide additional validation on the password check. Specifically you should create:a.Password update Form –This Python form allows a previously registered user to reset theirpassword after they have successfully logged in.

bAuthenticationfunctions–These Python functionswill check the following NIST SP 800-63B criteriaare met upon password update: Use the previous criteria for password length and complexity. (This work should already be done.) Compare the prospective secrets against a list that contains values known to be commonly-used, expected, or compromised (Provided as CommonPasswords.txt). If the chosen secret is found in the list, the application SHALL advise the subscriber thatthey need to select a different secret.

Logger –Create a log to log all failed login attempts. The Log should include date, time and IP address.
