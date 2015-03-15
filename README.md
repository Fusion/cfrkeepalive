# cfrkeepalive
An incredibly tiny set of three scripts to report remote hosts heartbeat to hashicorp's consul

This is for hosts that cannot talk to consul's cluster directly to keep it informed that they are still alive.

We have:

- a python script, running as a daemon that will poke a remote php script
- said php script, which will then update a local file (you will have to change paths!)
- a consul plug in to reference in `/etc/consul.d/host.json` 

Do not forget to synchronize your servers or you will have to add some time drift in there.
