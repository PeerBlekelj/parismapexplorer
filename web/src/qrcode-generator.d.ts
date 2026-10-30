// The package's own types describe the UMD build (`export =`), which this project cannot import
// under verbatimModuleSyntax. The ESM build is imported directly instead, and exports `qrcode` by
// name; this is the part of its surface the site uses.

declare module 'qrcode-generator/qrcode.mjs' {
  export interface QRCode {
    addData(data: string, mode?: 'Numeric' | 'Alphanumeric' | 'Byte' | 'Kanji'): void;
    make(): void;
    getModuleCount(): number;
    isDark(row: number, col: number): boolean;
  }
  /** `typeNumber` 0 picks the smallest symbol the data fits in. */
  export const qrcode: (typeNumber: number, errorCorrectionLevel: 'L' | 'M' | 'Q' | 'H') => QRCode;
}
