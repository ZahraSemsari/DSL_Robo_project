from __future__ import annotations

import argparse
import json
from antlr4 import FileStream, CommonTokenStream

from src.generated.RobotDSLLexer import RobotDSLLexer
from src.generated.RobotDSLParser import RobotDSLParser

from src.ast_builder_listener import build_ast
from src.codegen_python import generate_python

# اگر semantic را نگه می‌داری:
from src.semantic import analyze


def parse(path: str):
    inp = FileStream(path, encoding="utf-8")
    lexer = RobotDSLLexer(inp)
    tokens = CommonTokenStream(lexer)
    parser = RobotDSLParser(tokens)
    return parser.program()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--behavior", default=None)

    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("ast")
    sub.add_parser("check")

    genp = sub.add_parser("genpy")
    genp.add_argument("--out", default="generated_robot.py")

    args = ap.parse_args()

    tree = parse(args.file)
    program = build_ast(tree)

    if args.cmd == "ast":
        print(json.dumps(program.to_dict(), ensure_ascii=False, indent=2))
        return

    if args.cmd == "check":
        errs = analyze(program)
        if not errs:
            print("OK: no semantic errors")
            return
        for e in errs:
            print(e)
        raise SystemExit(1)

    if args.cmd == "genpy":
        # توصیه: قبل از تولید، semantic را چک کن
        errs = analyze(program)
        if errs:
            for e in errs:
                print(e)
            raise SystemExit(1)

        code = generate_python(program, behavior_name=args.behavior)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"generated -> {args.out}")


if __name__ == "__main__":
    main()
