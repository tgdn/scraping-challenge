import { API_URL } from "@/lib/constants";
import fetcher from "@/lib/fetcher";
import useSWR from "swr";

export function useHistory(id) {
  const { data, error } = useSWR(`${API_URL}/scrapes/${id}`, fetcher);

  return {
    scrape: data,
    isLoading: !error && !data,
    isError: error,
  };
}
