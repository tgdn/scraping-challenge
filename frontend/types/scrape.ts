export interface IScrape {
  url: string;
  created_at: string;
  completed_at?: string;
  error: boolean;
}

export interface IWordCount {
  scrape?: any;
  word: string;
  count: number;
}
