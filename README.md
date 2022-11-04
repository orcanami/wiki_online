# Wikipedia Online Status Updater
This is a tool to update your user page automatically based on your last Wikipedia edit. To use this script, a UserStatus template must be active on your Wikipedia user page. 
* If you have not edited for 10 minutes, your status is set to `away`.
* If you have editing within the past 10 minutes, your status is set to `online`.

## Setting up your Wikipedia page
* Create a User:<WP_USERNAME>/Status page.
* Follow instructions on the [UserStatus template page](https://en.wikipedia.org/wiki/Template:UserStatus).
* Add the user status template to your User:<WP_USERNAME> page.

## Running locally
* Clone the repository.
* Initialize a file `user_data.json` with a dictionary containing "username" and "password".
* Test your user page by making a recent edit and setting your status to `away` manually.
* Run `crontab -e`.
* Add the following line `3 *  * * *  bash /absolute/path/to/onlinebot/run_wiki_online.sh 2>>/tmp/errors1`
