import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.sound.midi.InvalidMidiDataException;
import javax.sound.midi.MidiUnavailableException;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

/**
 * Executable commands for music playback in the JTunes.
 */
public class Execution {
	/**
	 * Quit the current running player process.
	 * 
	 * @param player
	 *            : the player process that needs to be terminated
	 */
	public static void quit(AudioPlayer player) {
		try {
			player.close();
		} catch (NullPointerException npe) {
		} finally {
			System.out.println();
			System.out.println("Program ends here...");
			System.out.println();
		}
	}

	/**
	 * Create a playlist with the given songs' indexes.
	 * 
	 * @param userInput
	 *            : a branch of strings that is input by user, containing the
	 *            numbers of songs and the name of the playlist
	 * @param library
	 *            : the name for the music library with songs inside
	 * 
	 * @return the music library for screen display
	 */
	@SuppressWarnings("finally")
	public static MusicLibrary createPlaylist(String userInput,
			MusicLibrary library) {
		String[] userInputSplited = userInput.split(" ");
		String playlistName = userInputSplited[2];
		try {
			// Separate the user input into accessible format
			userInputSplited = userInputSplited[3].substring(1,
					userInputSplited[3].length() - 1).split(",");
		} catch (IndexOutOfBoundsException e) {
			System.out.println("Invalid command.\n");
		}

		library.displayAllLibrarySongs();
		System.out.println();

		try {
			// Create a playlist by the indexes entered by user.
			library.createPlaylist(playlistName, userInputSplited);
			library.displayAllLibraryPlaylists();
		} catch (IndexOutOfBoundsException e) {
			System.out
					.println("At least one song you want to include in the playlist does not exist in music library. Please try again.");
		} finally {
			return library;
		}

	}

	/**
	 * Play a particular song from the designated playlist with its name given.
	 * 
	 * @param library
	 *            : the music library containing songs
	 * @param player
	 *            : the called music player process
	 * @param playlist
	 *            : the name of the playlist
	 * @param index
	 *            : index numbers of wanted songs in the playlist
	 * 
	 * @return playback on the corresponding playlist
	 */
	public static AudioPlayer playPlaylistSong(MusicLibrary library,
			AudioPlayer player, String playlist, int index)
			throws NullPointerException, IndexOutOfBoundsException,
			MidiUnavailableException, InvalidMidiDataException, IOException {
		// Find the playlist in library by its name
		Playlist pl = library.findPlaylist(playlist);
		// Play the song in pl by the index entered by user
		return Execution.playPlaylistSong(library, player, pl, index);
	}

	/**
	 * Play a particular song from the designated playlist.
	 * 
	 * @param library
	 *            : the music library containing songs
	 * @param player
	 *            : the called music player process
	 * @param pl
	 *            : the needed playlist
	 * @param index
	 *            : index numbers of wanted songs in the playlist
	 * 
	 * @return a playback action with the certain song
	 */
	public static AudioPlayer playPlaylistSong(MusicLibrary library,
			AudioPlayer player, Playlist pl, int index)
			throws IndexOutOfBoundsException, MidiUnavailableException,
			InvalidMidiDataException, IOException {
		// Find the index of the song in library
		int songIndex = pl.findSong(index);
		// Play the song at position songIndex
		return Execution.playSong(library, player, songIndex);
	}

	/**
	 * Play a particular song in the playlist.
	 * 
	 * @param library
	 *            : the music library that contains songs
	 * @param player
	 *            : the audio player object
	 * @param index
	 *            : index number of the wanted song
	 * 
	 * @return a player dealing with that song
	 */
	public static AudioPlayer playSong(MusicLibrary library,
			AudioPlayer player, int index) throws IndexOutOfBoundsException,
			MidiUnavailableException, InvalidMidiDataException, IOException {
		try {
			// Stop the song if there is a previous song playing
			player.close();
		} catch (NullPointerException npe) {
		}
		// Play the song in library given index of the song
		player = new AudioPlayer(library.findSong(index));
		player.play();
		return player;
	}

	/**
	 * Delete an existing playlist given playlist's name.
	 * 
	 * @param library
	 *            : the music library containing that playlist
	 * @param userInput
	 *            : the input with the name of the playlist that needs deletion
	 * 
	 * @return a new music library with that playlist removed
	 */
	public static MusicLibrary deletePlaylist(MusicLibrary library,
			String userInput) {
		// Separate the userInput to accessible form.
		String[] userInputSplited = userInput.split(" ");
		String playlist = userInputSplited[2];

		// Delete playlist in library.
		if (library.deletePlaylist(playlist)) {
			// Tell the user if the playlist is deleted.
			System.out.println("playlist " + playlist + " has been deleted.");
		}
		library.displayAllLibrarySongs();
		System.out.println();
		library.displayAllLibraryPlaylists();
		return library;
	}

	/**
	 * Given an artist, find all his songs.
	 * 
	 * @param library
	 *            : the music library containing songs
	 * @param userInput
	 *            : the user input designating the artist
	 * 
	 * @return the music library for screen display
	 */
	public static MusicLibrary findSongByArtist(MusicLibrary library,
			String userInput) {
		String[] userInputSplited = userInput.split(" ");
		String artist = userInputSplited[3];
		// Find all the songs in library by the given artist
		library.findSongsByArtist(artist);
		library.displayAllLibrarySongs();
		System.out.println();
		library.displayAllLibraryPlaylists();
		return library;
	}

	/**
	 * Randomize the indexes of given songs.
	 * 
	 * @param indexes
	 *            : an array of indexes of songs covered
	 * 
	 * @return the new array of randomized indexes
	 */
	public static List<Integer> randomize(List<Integer> indexes) {
		Collections.shuffle(indexes);
		return indexes;
	}

	/**
	 * Randomly the songs in given indexes in random order.
	 * 
	 * @param library
	 *            : the music library containing songs
	 * @param player
	 *            : the audio player object
	 * @param indexes
	 *            : an array of the index of songs that need to be played
	 * 
	 * @return an audio player with songs being played
	 */
	public static AudioPlayer playRandom(MusicLibrary library,
			AudioPlayer player, List<Integer> indexes)
			throws IndexOutOfBoundsException, MidiUnavailableException,
			InvalidMidiDataException, IOException {
		indexes = Execution.randomize(indexes);
		// Play the song with randomized list of song indexes.
		for (Integer i : indexes) {
			player = Execution.playSong(library, player, i);
			// Check if the song is stil playing before playing the next song.
			player.checkIfRunning();
		}
		return player;

	}

	/**
	 * Randomly play a song in a specific playlist.
	 * 
	 * @param library
	 *            : the music library containing songs
	 * @param player
	 *            : the audio player object
	 * @param pl
	 *            : the playlist containing designated songs
	 * @param indexes
	 *            : an array of the index of wanted songs in the playlist
	 * 
	 * @return an audio player with songs being played
	 */
	public static AudioPlayer playRandom(MusicLibrary library,
			AudioPlayer player, Playlist pl, List<Integer> indexes)
			throws IndexOutOfBoundsException, MidiUnavailableException,
			InvalidMidiDataException, IOException {
		indexes = Execution.randomize(indexes);

		for (Integer i : indexes) {
			// Find the index of song in playlist from library, and play the
			// song.
			player = Execution.playPlaylistSong(library, player, pl, i);
			player.checkIfRunning();
		}
		return player;
	}

	/**
	 * Create a user with given name, e-mail address and password
	 * 
	 * @param name
	 *            : the username given by the user
	 * @param email
	 *            : the e-mail address given by the user
	 * @param pass
	 *            : the designated password
	 * 
	 * @return a boolean value whether the creation is done successfully
	 */
	public static boolean createUser(String name, String email, String pass) {
		// Concatenate user's information to url.
		String url = "http://greywolf.cdf.toronto.edu:1337/pineapple/createUser?name="
				+ name + "&email=" + email + "&password=" + pass;
		// Create the user in jCloud with given information.
		return Jcloud.createUser(url);
	}

	/**
	 * Try to open the url with given user's email and password to see whether
	 * the connection was successful.
	 * 
	 * @param email
	 *            : the e-mail address, which can be treated as a username
	 * @pass: the corresponding password
	 * 
	 * @return a downloading of all songs held by this user if it is valid.
	 */
	public static boolean varifyUser(String email, String pass) {
		String url = "http://greywolf.cdf.toronto.edu:1337/pineapple/listSongs?&email="
				+ email + "&password=" + pass;
		// Try to open the url with given information
		return Jcloud.listDownloadedSongs(url);
	}

	/**
	 * Save all the song names in playlists the user created to a xml file,
	 * named as email.xml.
	 * 
	 * @param email
	 *            : the e-mail address of the user
	 * @param playlists
	 *            : an array of all playlists created by this user
	 */
	public static void writePlaylistsToFile(MusicLibrary library) {
		// Create a new XML document.
		Document doc = openXml().newDocument();
		// Create Nodes that will be stored in doc.
		Element rootElement = doc.createElement("User");
		String email = library.getUseremail();
		rootElement.setAttribute("email", email);
		doc.appendChild(rootElement);
		ArrayList<Playlist> playlists = library.getPlaylists();

		for (int i = 0; i < playlists.size(); i++) {
			// Loop through all the playlists the user created
			Playlist playlist = playlists.get(i);
			Element plElement = doc.createElement("Playlist");
			plElement.setAttribute("name", playlist.getName());
			int[] indexes = playlist.getIndexes();
			// Loop through all the song indexes in playlist
			for (int j = 0; j < indexes.length; j++) {
				Element songElement = doc.createElement("Song");
				// Find the song title, and append to doc
				songElement.appendChild(doc.createTextNode(library
						.getTitle(indexes[j])));
				plElement.appendChild(songElement);
			}

			rootElement.appendChild(plElement);
		}

		// Transform the document doc to a XML file
		TransformerFactory transformerFactory = TransformerFactory
				.newInstance();
		Transformer transformer = null;
		try {
			transformer = transformerFactory.newTransformer();
		} catch (TransformerConfigurationException e) {
			e.printStackTrace();
		}
		DOMSource source = new DOMSource(doc);
		// Create new XML file named email.xml
		StreamResult result = new StreamResult(new File(email + ".xml"));
		try {
			transformer.transform(source, result);
		} catch (TransformerException e) {
			e.printStackTrace();
		}
	}

	/**
	 * A helper function that will create a new document builder
	 * 
	 * @return a newly created DocumentBuilder
	 */
	public static DocumentBuilder openXml() {
		// Create a new DocumentBuilderFactory and DocumentBuilder
		DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
		DocumentBuilder dBuilder = null;
		try {
			dBuilder = dbFactory.newDocumentBuilder();
		} catch (ParserConfigurationException e) {
			e.printStackTrace();
		}
		return dBuilder;
	}

	/**
	 * Read the xml file that contains all the playlists, and all the names of
	 * the songs in them.
	 * 
	 * @param library
	 *            : the main music library.
	 * 
	 * @return the updated music library with all the playlists.
	 */
	public static MusicLibrary readPlaylistXml(MusicLibrary library) {
		// Open the file containing playlists the user previously created
		File fXmlFile = new File(library.getUseremail() + ".xml");

		Document doc = null;
		try {
			// Open the file in Document format
			doc = Execution.openXml().parse(fXmlFile);
		} catch (FileNotFoundException e) {
			return library;
		} catch (SAXException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		doc.getDocumentElement().normalize();
		// Find all the playlist nodes and loop through it
		NodeList playlists = doc.getElementsByTagName("Playlist");
		for (int i = 0; i < playlists.getLength(); i++) {
			Node playlist = playlists.item(i);
			NodeList songs = ((Element) playlist).getElementsByTagName("Song");
			int numOfSongs = songs.getLength();
			ArrayList<String> indexes = new ArrayList<String>();
			// Find all the song nodes and loop through to check whether the
			// song is still in library
			for (int j = 0; j < numOfSongs; j++) {
				int song = library.findSongByTitle(songs.item(j)
						.getTextContent());
				if (song >= 0) {
					// Add it to indexes if the song still exists in library
					indexes.add((song + 1) + "");
				}
			}
			String[] indexesArray = (String[]) indexes
					.toArray(new String[indexes.size()]);
			// Create the playlist with the songs' indexes
			library.createPlaylist(playlist.getAttributes().item(0)
					.getNodeValue(), indexesArray);
		}
		return library;
	}

}
