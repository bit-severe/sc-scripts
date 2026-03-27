# sc-scripts

Collection of SuperCollider sound design experiments, plus Python OSC scripts that drive and automate synth playback/recording.

## What is in this repo

- `sc_only/`: standalone `.scd` sketches and pattern experiments.
- `sound_design/additive/`: additive synthesis in SuperCollider with optional Python OSC control.
- `sound_design/subtractive/`: subtractive synthesis in SuperCollider with optional Python OSC control.
- `test/`: quick OSC communication tests between Python and SuperCollider.

## How it works

The Python scripts send OSC messages to SuperCollider (default `127.0.0.1:57120`) to trigger synths, modulate parameters, and optionally start/stop recordings.  
Run the matching `.scd` file in SuperCollider first so OSC receivers are active, then run the Python script.
