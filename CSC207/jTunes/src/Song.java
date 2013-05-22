import java.io.File;

/**
 * An implementation of a Song object that stores the song information.
 */
public class Song {
	/**
	 * The Song class creates a Song object which contains the midi file, song
	 * title and artist.
	 * 
	 */
	private String title;
	private String artist;
	private File aSong;

	public String getFileName() {
		return aSong.getName();
	}

	/**
	 * Create a Song object and initiate song information to specific variables.
	 * 
	 * @param midi
	 *            : the midi file.
	 * 
	 */
	public Song(File midi) {
		this.aSong = midi;

		String[] info = readMidiInfo(midi);
		this.title = info[0];
		this.artist = info[1];

	}

	/**
	 * Return the song's title and name of the artist.
	 * 
	 * @param midi
	 *            : the midi file.
	 * @return info: song's title and name in an array.
	 */
	private String[] readMidiInfo(File aSong) {

		String[] info = aSong.getName().split("&");
		return info;
	}

	/**
	 * Return the midi file of the song.
	 * 
	 * @return aSong: midi file
	 */
	public File getSource() {
		return this.aSong;
	}

	/**
	 * Return the title of the song.
	 * 
	 * @return title: the title of the song
	 */
	public String getTitle() {
		return title;

	}

	/**
	 * Return artist's name of the song.
	 * 
	 * @return artist: the name of the artist
	 */
	public String getArtist() {
		return artist;

	}

	/**
	 * Remove the song file in directory permanently.
	 */
	public boolean delete() {
		return (aSong.delete());

	}
}