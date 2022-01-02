window.onSpotifyWebPlaybackSDKReady = () => {
  // You can now initialize Spotify.Player and use the SDK
  const token = 'BQB4fDNghqns8xIVzFWtiJcH1b-G4sY8HJO6ABRYOdCJtPwzPFOAAtZZZ4TDnIRS-kgfr_Zy9R-7b5eamiXIcEMP_cK8CNNQnMoNJj4vGhvTzCKVf7s5PKOpq_ObcSjBLiIRutSdWBcg0wOLqjRt9PC7cR3PZfXu8gQ';
  const player = new Spotify.Player({
    name: 'Virtual Speaker',
    getOAuthToken: cb => { cb(token); },
    volume: 0.5
  });
// Ready
player.addListener('ready', ({ device_id }) => {
  console.log('Ready with Device ID', device_id);
});

// Not Ready
player.addListener('not_ready', ({ device_id }) => {
  console.log('Device ID has gone offline', device_id);
});

player.addListener('initialization_error', ({ message }) => { 
    console.error(message);
});

player.addListener('authentication_error', ({ message }) => {
    console.error(message);
});

player.addListener('account_error', ({ message }) => {
    console.error(message);
});        
player.connect();

document.getElementById('togglePlay').onclick = function() {
  console.log("hello")
  player.togglePlay();
};

}