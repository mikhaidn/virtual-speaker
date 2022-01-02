sudo apt-get install python3-pip
git clone git@github.com:mikhaidn/virtual-speaker.git


 ssh-keygen -t ed25519 -C "danmikhail+github.@gmail.com"
 cat /home/dmikhail/.ssh/id_ed25519.pub

curl -sS https://download.spotify.com/debian/pubkey_5E3C45D7B312C643.gpg | sudo apt-key add -
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
sudo apt-get update && sudo apt-get install spotify-client

generate SDK token at
