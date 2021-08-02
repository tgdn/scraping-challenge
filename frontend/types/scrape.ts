export interface IScrape {
  id: number;
  url: string;
  created_at: string;
  completed_at?: string;
  error: boolean;
}

export interface IWordCount {
  id: number;
  scrape?: any;
  word: string;
  count: number;
}
