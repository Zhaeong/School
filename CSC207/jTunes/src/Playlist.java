import java.util.ArrayList;

/**
 * An implementation of a default playlist that contains all the songs in
 * library. And an implementation of a playlist that stores all the indexes of
 * songs the user demand.
 */
public class Playlist {
	/**
	 * The Playlist class creates a Playlist that contains the index location of
	 * where the song is in the musiclibrary.
	 */
	private ArrayList<Integer> playlist;

	private String name;

	/**
	 * Create a playlist object.
	 * 
	 * @param name
	 *            :the name of the playlist.
	 */
	public Playlist(String name) {

		playlist = new ArrayList<Integer>();
		this.name = name;
	}

	/**
	 * Create a temporary playlist required in other methods.
	 */
	public Playlist() {

		playlist = new ArrayList<Integer>();

	}

	/**
	 * Return the length of the playlist
	 * 
	 * @return the length of the playlist.
	 */
	public int numberOfSongs() {

		return playlist.size();
	}

	/**
	 * Delete a particular song in the playlist given the song's index.
	 * 
	 * @param index
	 *            : the index number of the song that is about to be deleted.
	 */
	public void delSong(int index) {
		// loop through playlist and delete the song with the same index
		for (int x = 0; x < this.playlist.size(); x++) {
			if (playlist.get(x) == index) {
				playlist.remove(x);
			}
		}
	}

	/**
	 * Return a particular song in the playlist given the song's index.
	 * 
	 * @return index: the index number of where the song is at in the playlist.
	 */
	public int findSong(int index) {
		return playlist.get(index);
	}

	/**
	 * Add a new song at given index to the playlist.
	 * 
	 * @param index
	 *            : the index location of where the song is located in the music
	 *            libaray.
	 * 
	 */
	public void addSong(int index) {
		playlist.add(index);
	}

	/**
	 * Return the name of the playlist.
	 * 
	 * @return name.
	 */
	public String getName() {
		return this.name;
	}

	/**
	 * Get all the songs' indexes in playlist.
	 * 
	 * @return indexes : int[] that contains all the songs' indexes.
	 */
	public int[] getIndexes() {
		int length = playlist.size();
		int[] indexes = new int[length];
		// Loop through the playlist and get the indexes
		for (int i = 0; i < length; i++) {
			indexes[i] = playlist.get(i);
		}
		return indexes;
	}

}
