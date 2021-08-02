import { API_URL } from "@/lib/constants";
import fetcher from "@/lib/fetcher";
import useSWR from "swr";

export function useHistory() {
  const { data, error } = useSWR(`${API_URL}/scrapes`, fetcher);

  return {
    history: data,
    isLoading: !error && !data,
    isError: error,
  };
}
