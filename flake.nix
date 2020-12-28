{
  description = "Web-based data visualizer for UT boards burn-in.";

  inputs = rec {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-20.09";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python3;
        pythonPackages = python.pkgs;
        stdenv = pkgs.stdenv;
      in
      rec {
        packages = rec {
          DataVisualizer = python.withPackages (ps: with ps; [
            bokeh
            pyyaml
          ]);
          DataVisualizer_Dev = pkgs.mkShell {
            buildInputs = [ DataVisualizer ]
            ++ stdenv.lib.optionals (stdenv.isx86_64) (with pythonPackages; [
              # Python auto-complete
              jedi

              # Linters
              flake8
              pylint
            ]);
          };
        };
        devShell = packages.DataVisualizer_Dev;
      });
}
