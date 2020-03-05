## Postbook
### Flag 1
#### After logging in, you can see a post made by someone with the username "user" and the username "admin". If someone creates an account with the username "user", what would there password be? Sign in with the username "user" and the password "password" to get the first flag.
### Flag 2
#### Open up any post and you can see the URL end with ...id=somenumber. Change this to different numbers, you can view different posts, maybe even hidden posts. Change the id to 2, and you can get the second flag. 
### Flag 3
#### Open up the form to create a new post, and then inspect element. In the HTML, there is a field for user-id set to hidden, make it visible, and that will open a testbox with your user id. Change this to 1 or 2, and create your post. This will allow you to create a post under someone else's username.
### Flag 4
#### On the main page, inspect element on the edit button of your post. The edit button references a page that ends with an id. Change this id to 1, and you will be able to edit the admin's post. Click submit and the fourth flag will appear. 
### Flag 5
#### This flag requires you to manipulate cookies. Open up burpsuite and set up your proxy on firefox. When you login, you can see the contents of your cookie. In the id field, there is a id=somemd5checksum, change this to the md5 hash for 1, and you will be able to login as admin. 
### Flag 6
#### Inspect element on the delete button and the id the button references is a md5 checksum. It seems the delete button uses a hash to identify which post to delete. Substituting this id with the md5 hash for 1, will allow you to delete the admin's post.