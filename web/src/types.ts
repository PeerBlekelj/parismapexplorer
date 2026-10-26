// Shapes of the two data files described in DATA_CONTRACT.md. The app reads nothing else.

export type PlaceType =
  | 'street' | 'church_religious' | 'college' | 'building' | 'gate_wall'
  | 'bridge' | 'square_market' | 'village_faubourg' | 'other';

export type Status = 'standing' | 'rebuilt' | 'renamed' | 'vanished';
export type LocConfidence = 'exact' | 'approx' | 'uncertain';

export interface Source { label: string; url: string }

export interface Place {
  id: string;
  old: string;
  type: PlaceType | string;
  px: [number, number];
  orient: 'h' | 'v' | 'd' | string;
  flag: 'ok' | 'unsure' | string;
  note: string | null;
  modern: string | null;
  status: Status | string | null;
  lat: number | null;
  lon: number | null;
  loc_confidence: LocConfidence | string | null;
  summary: string | null;
  variants: string[];
  sources: Source[];
}

export interface PlacesFile {
  generated: string;
  image: { width: number; height: number; orientation: string };
  places: Place[];
}

export interface Gcp {
  id: string;
  name: string;
  px: [number, number];
  lat: number;
  lon: number;
  quality: string;
}

export interface GcpsFile { generated?: string; gcps: Gcp[] }

export type Vec2 = [number, number];
