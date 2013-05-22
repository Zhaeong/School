import java.io.*;
import java.net.URL;
import java.net.URLConnection;
import java.util.*;

/**
 * An implementation of a Music library that contains all the songs, playlists,
 * and audio player. The music library is responsible for organizing songs in
 * directory, or displaying to user, based on the user's commands.
 */
public class MusicLibrary {
	/**
	 * MusicLibrary class creates a library that contains all songs, all
	 * playlists, and all information on iClouds.
	 * 
	 */
	private static MusicLibrary instance = null;
	private ArrayList<Song> songs;
	private ArrayList<Playlist> playlists;
	private String userpass;
	private String useremail;
	private List<String> jCloudSongs;

	/**
	 * Create a MusicLibrary, and initiate all components required for accessing
	 * user's commands.
	 * 
	 * @param email
	 *            : user's email address
	 * @param pass
	 *            : user's password
	 * @throws IOException
	 */
	private MusicLibrary(String pass, String email) throws IOException {
		this.userpass = pass;
		this.useremail = email;

		// initialize songs, playlists and jCloudSong that will store all the
		// songs, playlists, and song information from jCloud respectively
		songs = new ArrayList<Song>();
		playlists = new ArrayList<Playlist>();
		jCloudSongs = new ArrayList<String>();

		loadLibaray(System.getProperty("user.dir"));
		System.out.println(".");
		loadJCloudInfo();
	}

	/**
	 * Making musiclibrary object a singleton. return a new musiclibrary object
	 * if no music object was created. return the existing musiclibrary if one
	 * is already being created.
	 * 
	 * @param email
	 *            : user's email address
	 * @param pass
	 *            : user's password
	 * @throws IOException
	 */
	public static MusicLibrary getMusicLibrary(String pass, String email)
			throws IOException {
		// This is useful when exactly one object is needed to coordinate
		// actions across the system
		if (MusicLibrary.instance == null) {
			MusicLibrary.instance = new MusicLibrary(pass, email);
		}

		return MusicLibrary.instance;

	}

	/**
	 * return the list of every song in music library in ArrayList<String>.
	 * 
	 * @return songs : An ArrayList<String> that contains all the songs in
	 *         library.
	 */
	public ArrayList<Song> getListOfAllSong() {
		return songs;
	}

	/**
	 * Create a user-defined playlist and add to the list of playlists which
	 * comprises the library.
	 * 
	 * @param name
	 *            : the name of the playlist given by user input.
	 * @param indexes
	 *            : the index locations of where the songs are located in the
	 *            music library.
	 * 
	 */
	public void createPlaylist(String name, String[] indexes) {
		// create a new playlist
		Playlist playlist = new Playlist(name);

		// loop through the given song indexes and add to the new playlist
		for (int n = 0; n < indexes.length; n++) {
			if (Integer.parseInt(indexes[n]) > songs.size()) {
				throw new IndexOutOfBoundsException();
			} else {
				playlist.addSong(Integer.parseInt(indexes[n]) - 1);
			}
		}
		if (this.findPlaylist(name) != null) {
			this.deletePlaylist(name);
		}
		playlists.add(playlist);
	}

	/**
	 * Load the music library from a certain path. And add all the midi files
	 * found to the library.
	 * 
	 * @param path
	 *            : the directory of where the songs are.
	 * 
	 */
	public void loadLibaray(String path) {
		// loop through the current directory to find all the midi files and add
		// to songs
		File reader = new File(path);

		File[] songsTemp = reader.listFiles();

		for (int i = 0; i < songsTemp.length; i++) {
			if (songsTemp[i].isFile()) {
				if (songsTemp[i].getName().endsWith(".mid")) {
					this.songs.add(new Song(songsTemp[i]));
				}
			}
		}
	}

	/**
	 * Load information of the songs from JCloud. And store the information in
	 * jCloudSongs.
	 * 
	 * @throws IOException
	 */
	public void loadJCloudInfo() throws IOException {
		jCloudSongs = Jcloud.listSongs(jCloudSongs);
	}

	/**
	 * Display all available songs in the music library with title and artist.
	 * 
	 */
	public void displayAllLibrarySongs() {
		String header[] = new String[20];
		String borad[][] = new String[songs.size()][15];
		header[3] = "Name:";
		header[17] = "Artist:";
		for (int row = 0; row < header.length; row++) {
			if (header[row] == null) {
				System.out.print(" ");
			} else {
				System.out.print(header[row]);
			}
		}
		// loop through and display all songs stored in library
		for (int row = 0; row < songs.size(); row++) {

			for (int column = 0; column < 14; column++) {
				if (column == 0) {
					borad[row][column] = Integer.toString(row + 1);
				} else if (column == 3) {
					borad[row][column] = songs.get(row).getTitle();
				} else if (column == 13) {
					borad[row][column] = songs.get(row).getArtist();
				}
			}
		}

		System.out.println();
		for (int row = 0; row < borad.length; row++) {
			for (int column = 0; column < borad[row].length; column++) {
				if (borad[row][column] == null) {
					System.out.print(" ");
				} else {
					System.out.print(borad[row][column]);
				}
			}
			System.out.println();
		}
	}

	/**
	 * Display all available songs for download in JCloud.
	 * 
	 */
	public void displayJcloudSongs() {
		// loop through jCloudSongs and display the song name and its artist
		Jcloud.listSongs();
	}

	/**
	 * Display all available playlists created by user in the music library.
	 */
	public void displayAllLibraryPlaylists() {
		// loop through and display all playlists stored in library
		Iterator<Playlist> mainIterator = playlists.iterator();
		while (mainIterator.hasNext()) {
			Playlist list = mainIterator.next();

			System.out.println(list.getName());

			for (int n = 0; n < list.numberOfSongs(); n++) {
				System.out.println(n + 1 + ". "
						+ songs.get(list.findSong(n)).getTitle());
			}
			System.out.println();
		}

	}

	/**
	 * Get the title of the song located in music library given the song's
	 * index.
	 * 
	 * @param index
	 *            : the index number of the song
	 * 
	 * @return the title of the song
	 */
	public String getTitle(int index) {
		return songs.get(index).getTitle();
	}

	/**
	 * Given the index of the playlist, return the name of the playlist created
	 * by the user in the list of playlists.
	 * 
	 * @param index
	 *            : the index number of a playlist
	 * 
	 * @return the name of this playlist
	 */

	public String getPlaylistName(int index) {
		return this.playlists.get(index).getName();
	}

	/**
	 * return whether the music library contains the song, given its title.
	 * 
	 * @param songTitle
	 *            : the name of the song that needs to be determined
	 * 
	 * @return boolean : Whether the song is in the library.
	 */
	public boolean contains(String songTitle) {
		// loop through and check if library contains a specific song
		for (int i = 0; i < this.numberOfSongs(); i++) {
			if (this.songs.get(i).getFileName().equals(songTitle)) {
				return true;
			}
		}
		return false;
	}

	/**
	 * Return the song object given the song's index.
	 * 
	 * @param index
	 *            : the index location of where the song is in the music
	 *            library.
	 * @throws IndexOutOfBoundsException
	 * @return the song object specified by index.
	 */
	public Song findSong(int index) throws IndexOutOfBoundsException {
		return songs.get(index);
	}

	/**
	 * Return the playlist given its name.
	 * 
	 * 
	 * @param name
	 *            : name of the playlist
	 * 
	 * @return playlist: Return the playlist object if found.
	 * @return null: if the playlist is not found.
	 */
	public Playlist findPlaylist(String name) {
		// loop through and find the playlist with given name
		for (Playlist playlist : playlists) {
			if (playlist.getName().equals(name)) {
				return playlist;
			}
		}
		// return null if playlist is not found
		return null;
	}

	/**
	 * Delete a particular playlist by the name given. If the playlist is
	 * deleted successfully, notify the user If the playlist does not exist in
	 * the list of playlists, then notify the user.
	 * 
	 * @param name
	 *            : the name of the playlist that needs to be removed.
	 * 
	 */
	public boolean deletePlaylist(String name) {
		// loop through and remove the playlist with the given name
		boolean deleted = false;
		int a = playlists.size();
		for (int n = 0; n < playlists.size(); n++) {
			if (name.equals(playlists.get(n).getName())) {
				playlists.remove(n);
				deleted = true;
			}
		}
		if (a == playlists.size()) {
			System.out.println();
			System.out
					.println("The playlist you are about to delete does not exist in your music library.");
			System.out.println();
		}
		return deleted;
	}

	/**
	 * Download a song from JCloud given the song's title. And save it as
	 * title&artist&.mid in current directory.
	 * 
	 * @param title
	 *            : the title of song to be downloaded.
	 * 
	 * @throws NullPointerException
	 */
	public void downloadSong(String title) throws NullPointerException,
			IOException {
		int index = jCloudSongs.indexOf(title);// search for the song that the
		// user wants to download if it
		// exists.
		if (index != -1) {
			// int index = jCloudSongs.indexOf(title);
			String sid = this.jCloudSongs.get(index + 1);
			String artist = this.jCloudSongs.get(index + 2);
			// store the file in a specific format the program can recognize
			String filename = title + "&" + artist + "&" + ".mid";
			// check if local directory already contains the file before
			// downloading
			// the song
			if (!this.contains(filename)) {
				String url = "http://greywolf.cdf.toronto.edu:1337/pineapple/getSong?email="
						+ this.useremail
						+ "&passwo"
						+ "rd="
						+ this.userpass
						+ "&songid=" + sid;
				// connect and open inputStream from url
				Jcloud.getSong(url, filename);
				Song newSong = new Song(new File(filename));
				songs.add(newSong);
				System.out.println(title + " download completed.");
			} else {
				System.out.println(title + " already existed in folder.");
			}
		} else {
			System.out
					.println("the song "
							+ title
							+ " that you want to download does not exist in jTunes web service.");
		}
	}

	/**
	 * Download all songs the user previously downloaded from JCloud.
	 * 
	 * @throws NullPointerException
	 */
	public void downloadPreviousSongs() throws NullPointerException,
			IOException {
		String url = "http://greywolf.cdf.toronto.edu:1337/pineapple/listSongs?email="
				+ this.useremail + "&password=" + this.userpass;
		List<String> downloadedSongs = new ArrayList<String>();
		downloadedSongs = Jcloud.listDownloadedSongs(url, downloadedSongs);
		//Loop through downloadedSongs and download each song to current directory.
		for (int i = 0; i < downloadedSongs.size(); i++) {
			int index = jCloudSongs.indexOf(downloadedSongs.get(i));
			if (index > -1) {
				this.downloadSong(jCloudSongs.get(index - 1));
			}
		}
	}

	/**
	 * Find all songs by a given artist and add them to a playlist. the
	 * playlist's name is the artist's name. notify user if the artist name give
	 * does not exist.
	 * 
	 * @param artist
	 *            : the name of the artist.
	 * 
	 */
	public void findSongsByArtist(String artist) {
		Playlist l = new Playlist(artist);
		// loop through songs to find songs by given artist
		// if matches, store it in a new playlist
		for (int n = 0; n < songs.size(); n++) {
			if (songs.get(n).getArtist().equals(artist)) {
				l.addSong(n);
			}
		}
		// tell the user if none of the songs are by this artist
		if (l.numberOfSongs() == 0) {

			System.out.println("artist name does not exist, please try again.");
			System.out.println();

		} else {
			// if the playlist is not empty, store this playlist
			playlists.add(l);
		}

	}

	/**
	 * Find and return all the songs by the title given (this method is not
	 * currently being used)
	 * 
	 * @param title
	 *            : the title of the song
	 * @return: song: the corresponding song if it exists.
	 * @return: null: return null if the song does not exist.
	 */
	public int findSongByTitle(String title) {
		// loop through and return the song with the given title
		Song song;
		for (int i = 0; i < songs.size(); i++) {
			song = songs.get(i);
			if (song.getTitle().equals(title)) {
				return i;
			}
		}
		// return null if song is not found
		return -1;
	}

	/**
	 * Return the number of songs that exist in the music library.
	 * 
	 * @return size: total number of songs in the music library.
	 */
	public int numberOfSongs() {
		int size = songs.size();
		return size;
	}

	/**
	 * Delete a song from the music library according to the index location
	 * given.
	 * 
	 * @param index
	 *            : the index number of where the song is in the music library.
	 */
	public void delSong(int index) {
		songs.get(index).delete();
		songs.remove(index);

	}

	/**
	 * Return the list of playlists
	 * 
	 * @return playlists
	 */
	public ArrayList<Playlist> getPlaylists() {
		return playlists;
	}

	/**
	 * Return the user email
	 * 
	 * @return: useremail
	 */
	public String getUseremail() {
		return this.useremail;
	}
}
