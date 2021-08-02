import { useRouter } from "next/router";
import { useScrape } from "./useScrape";

export default function DetailView() {
  const {
    query: { id },
  } = useRouter();
  const { scrape, isLoading, isError } = useScrape(id);

  return (
    <div className="mt-4">
      <h1 className="text-2xl text-center font-medium mb-2">Detail</h1>
      {isLoading ? (
        <p>Loading...</p>
      ) : isError ? (
        <p>Could not fetch</p>
      ) : (
        <h2 className="text-xl text-gray-700">{scrape.url}</h2>
      )}
    </div>
  );
}
