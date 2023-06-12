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

## Progress

- Peripherals
    - [x] Registers
    - [x] Memory
    - [ ] Keyboard
    - [ ] Display
    - [ ] Sound timer
    - [ ] Delat timer
- Instructions
    - [ ] 00E0 - CLS
    - [x] 00EE - RET
    - [x] 0nnn - SYS addr
    - [x] 1nnn - JP addr
    - [x] 2nnn - CALL addr
    - [x] 3xkk - SE Vx, byte
    - [x] 4xkk - SNE Vx, byte
    - [x] 5xy0 - SE Vx, Vy
    - [x] 6xkk - LD Vx, byte
    - [x] 7xkk - ADD Vx, byte
    - [x] 8xy0 - LD Vx, Vy
    - [x] 8xy1 - OR Vx, Vy
    - [x] 8xy2 - AND Vx, Vy
    - [x] 8xy3 - XOR Vx, Vy
    - [x] 8xy4 - ADD Vx, Vy
    - [x] 8xy5 - SUB Vx, Vy
    - [x] 8xy6 - SHR Vx {, Vy}
    - [x] 8xy7 - SUBN Vx, Vy
    - [x] 8xyE - SHL Vx {, Vy}
    - [x] 9xy0 - SNE Vx, Vy
    - [x] Annn - LD I, addr
    - [x] Bnnn - JP V0, addr
    - [x] Cxkk - RND Vx, byte
    - [ ] Dxyn - DRW Vx, Vy, nibble
    - [ ] Ex9E - SKP Vx
    - [ ] ExA1 - SKNP Vx
    - [x] Fx07 - LD Vx, DT
    - [ ] Fx0A - LD Vx, K
    - [x] Fx15 - LD DT, Vx
    - [x] Fx18 - LD ST, Vx
    - [x] Fx1E - ADD I, Vx
    - [ ] Fx29 - LD F, Vx
    - [x] Fx33 - LD B, Vx
    - [x] Fx55 - LD [I], Vx
    - [x] Fx65 - LD Vx, [I]
- Extra features (nice to haves)
    - [ ] Multiple ROM loading
    - [ ] Custom button mapping
    - [ ] Super Chip-48 implementation
