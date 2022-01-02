window.onSpotifyWebPlaybackSDKReady = () => {
  const token = 'BQCrZzxaJdEWz7qbRR8XkY2ZpMKa_8V3L5wewht9RaeJLwHkFRr6UKfcLXdQszlMXX3DbehZomUhz27lMW1-mp9CIFeATQ_7J4Vk7bZ8ip_ZRVapwItmsyCddRwW6orHVQK1drZDfGFan12EwLCDBT_8qGVZ1PEhLis';
  const player = new Spotify.Player({
    name: 'Web Playback SDK Quick Start Player',
    getOAuthToken: cb => { cb(token); },
    volume: 0.5
  });
