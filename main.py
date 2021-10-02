#encode-utf8

#include file make by us
from Engine import Engine
from GameSocket import GameSocket

if __name__ == "__main__":
	socket = GameSocket()
	engine = Engine(socket)
	engine.run()