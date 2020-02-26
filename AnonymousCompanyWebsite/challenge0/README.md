## Challenge 0
#### This challenge is an SQL injection. The "Get Pages" button returns a list of animals. Going into the inspect element, there is a field labeled "hidden". Changing this to visible, creates a text box where the user is able to input their query. At the end of the URL, there is a "?key=xxxxxxx..." where the user can submit input as opposed to using the text box.
#### Solution: the input
>' or '1' = '1
#### dumps the flag along with the contents of the database. 