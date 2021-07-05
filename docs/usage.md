# Usage instructions

Start the web server.

```sh
$ make serve
```

Open the browser at:

- http://localhost:5000

The HTML and CSS has been written to be somewhat mobile responsive. So, if you have a mobile device connected to the network, you can use it view the service by following these steps:

1. Find your machine's IP address using `ip a` in the terminal and look for your IP address on the network. e.g. `192.168.8.10`.
2. Enter http://YOUR.IP.ADDRESS.HERE:5000 as the path in your mobile device's browser.
3. If you do not see anything, you may have to adjust your machine's firewall settings to allow incoming requests on your network for port 5000.


## Development

### Format

```sh
$ make fmt
```
