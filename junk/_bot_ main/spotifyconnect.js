window.onSpotifyWebPlaybackSDKReady = () => {
  // You can now initialize Spotify.Player and use the SDK
  const token = 'BQBmcCYmSmFxMKX7rpyCeeMNEVQo9ephKW2HXqAi4OUT7Xo7fKSwb83oIFJ2Ost9KYx2cKUB40SvdesjxX7SKPrfpwhdYG2CqR1y_35d84RvuZ09-C_KhvDuUXSpXRcmh5WQjvDmdxsfuKVQ67GFmCTL-NrFTLEKKY0';
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
