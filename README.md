# Chip8 emulator for the Gameboy
RGBDS assembler project with the goal of making a Chip8 emulator for the Gameboy.

Information on Chip can be found in 
[Cowgod's Chip-8 Technical Reference v1.0](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM).

Information on the RGBDS tools can be found on the
[RGBDS home page](https://rgbds.gbdev.io/).

## Building

Building is done using `make`.
The built Gameboy image can then be found at `build/chip8.gb`.

## Including roms

ROMs are kept in the `roms` directory.
To then include said ROM to the project,
add it to the file [src/roms.z80](src/roms.z80).

Including a file in RGBDS assembly is done using the `include` directive:

```asm
section "Chip8 Rom - chip8_example_rom", romx, bank[$01], align[$0C, $200]
c8_rom::
incbin "roms/chip8_example_rom.ch8"
```

Currently, the emulator only supports 1 ROM to be saved.
I'll maybe implement the ability to select a ROM at startup,
but that depends on my mood.