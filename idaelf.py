import lief
import idb
import argparse


def gen_lief_sym(func_addr, name):
    sym = lief.ELF.Symbol()
    sym.name = name
    sym.value = func_addr
    sym.type = lief.ELF.SYMBOL_TYPES.FUNC

    return sym


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extracts and adds symbols (function names for now) from IDBs to ELFs"
    )
    parser.add_argument("binary", type=str, help="binary to apply symbols to")
    parser.add_argument(
        "idb", type=str, help="IDB from which to apply symbols")
    parser.add_argument(
        "-o", "--output", type=str, default="a.symbols.out", help="output binary"
    )
    args = parser.parse_args()

    binary = lief.parse(args.binary)

    with idb.from_file(args.idb) as db:
        api = idb.IDAPython(db)
        for ea in api.idautils.Functions():
            name_in_ida = api.idc.GetFunctionName(ea)
            sym = gen_lief_sym(ea, name_in_ida)
            binary.add_dynamic_symbol(sym)

    binary.write(args.output)
