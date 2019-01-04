rm build/*
mkdir -p build/
python3 -m grpc_tools.protoc -I./src/ --python_out=./build/ --grpc_python_out=. ./src/*
mv *.py build/
echo "Compiled proto files. Installation is NOT complete."
echo "To finish the installation of the compiled proto files you must"
echo "replace all imports of _pb2 files in the _grpc files with proto.build.(name)_pb2."
echo "Example (from chain_pb2_grpc.py):"
echo "# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!"
echo "import grpc"
echo "import chain_pb2 as chain__pb2 --> import proto.build.chain_pb2 as chain__pb2"
echo "class ChainStub(object):"
echo "  ..."
echo "This must be done for all _grpc.py files."