import java.io.IOException;
import javax.sound.midi.InvalidMidiDataException;
import javax.sound.midi.MidiUnavailableException;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * An implementation of jTunes main method
 */
public class Jtunes {

	/**
	 * Calls helper methods to initiate the main music library.
	 * 
	 * @param args
	 * @throws FileNotFoundException
	 *             , InvalidMidiDataException,
	 *             IOException,MidiUnavailableException
	 */
	private static AudioPlayer player;
	private static MusicLibrary library;

	public static void main(String[] args) throws FileNotFoundException,
			InvalidMidiDataException, IOException, MidiUnavailableException {

		displayWelcomeMessage();
		createUserID();
		displayUserManual();
		library.displayAllLibrarySongs();
		executeUserCommand();

	}

	/**
	 * Informs the user whether the user has an account, login or create a new account with given information.
	 * 
	 * @throws IOException
	 * 
	 */

	private static void createUserID() throws IOException {
		InputStreamReader isr = new java.io.InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		// log in screen prompted at every start of program
		while (true) {
			// will prompt user for input until correct input is given, and then
			// exits the loop
			System.out.println("New User?(Enter 'yes', or 'no', or 'quit')");
			String newuser = br.readLine();
			if (newuser.equals("yes") || newuser.equals("no")) {

				System.out.println("Username: ");
				String username = br.readLine();

				System.out.println("Password: ");
				String userpass = br.readLine();

				System.out.println("Email: ");
				String useremail = br.readLine();

				boolean suc = false;
				if (newuser.equals("yes")) {
					// initializes main library where all player methods are
					// run through. Created based on user input
					suc = Execution.createUser(username, useremail, userpass);
				} else if (newuser.equals("no")) {
					suc = Execution.varifyUser(useremail, userpass);
				}
				if (suc) {
					library = MusicLibrary.getMusicLibrary(userpass, useremail);
					Execution.readPlaylistXml(library);
					break;
				}
			}

			else if (newuser.equals("quit")) {
				Execution.quit(player);
				System.exit(0);
			}
		}
	}

	/**
	 * Prompt the user for input and interpret the command recieved.
	 * 
	 * @throws MidiUnavailableException, InvalidMidiDataException
	 */

	public static void executeUserCommand() throws MidiUnavailableException,
			InvalidMidiDataException {

		while (true) {
			System.out.println();
			System.out.print("Enter User Command. (Type 'quit' to quit) ");
			System.out.println();
			InputStreamReader isr = new java.io.InputStreamReader(System.in);
			BufferedReader br = new BufferedReader(isr);

			try {
				String userInput = br.readLine();
				// the userInput is evaluated to different functions encased in
				// the following if blocks.
				// some functions take in user input and evaluates what the user
				// wants by separating it into different sections
				if (userInput.equals("quit")) {
					Execution.quit(player);
					Execution.writePlaylistsToFile(library);
					break;

				} else if (userInput.startsWith("create playlist")
						&& userInput.endsWith(")")) {
					library = Execution.createPlaylist(userInput, library);
					Execution.writePlaylistsToFile(library);

				} else if (userInput.startsWith("play playlist")) {
					String[] userInputSplited = userInput.split(" ");
					String playlist = userInputSplited[2];
					if (userInputSplited.length == 4
							& userInput.matches(".*\\d.*")) {
						// When input length is 4, then play specified song that
						// user inputs
						int songIndex;
						try {
							songIndex = Integer.parseInt(userInputSplited[3]) - 1;
						} catch (NumberFormatException nfe) {
							System.out
									.println("Please enter a valid index that is in this playlist. Please try again.");
							continue;
						}
						try {
							player = Execution.playPlaylistSong(library,
									player, playlist, songIndex);
						} catch (IndexOutOfBoundsException iobe) {
							System.out
									.println("Please enter a valid index that is in this playlist. Please try again.");
							continue;
						} catch (NullPointerException e) {
							System.out
									.println("Playlist does not exist. Please try again.");
							continue;
						}

					} else if (userInputSplited.length == 3
							| (!userInput.matches(".*\\d.*"))) {
						// if command does not contain integer, play entire
						// playlist
						Playlist pl;
						pl = library.findPlaylist(playlist);
						// checks if playlist exists
						if (pl == null) {
							System.out
									.println("Playlist does not exist. Please try again.");
							continue;
						}
						for (int i = 0; i < pl.numberOfSongs(); i++) {
							// plays the playlist songs one by one
							try {
								player = Execution.playPlaylistSong(library,
										player, pl, i);
							} catch (IOException e) {
								System.out.println("Midi file not available!");
							}
							player.checkIfRunning();
						}
					}

				} else if (userInput.startsWith("delete playlist")) {
					library = Execution.deletePlaylist(library, userInput);

				} else if (userInput.startsWith("find songs by")) {
					library = Execution.findSongByArtist(library, userInput);
				}

				else if (userInput.startsWith("play song")) {

					String[] userInputSplited = userInput.split(" ");
					int songIndex;
					try {
						songIndex = Integer.parseInt(userInputSplited[2]) - 1;
					} catch (NumberFormatException nfe) {
						// the user input can only be an integer
						System.out.println("Please enter a song index!");
						continue;
					}
					try {
						player = Execution.playSong(library, player, songIndex);
					} catch (IndexOutOfBoundsException iobe) {
						System.out
								.println("Song does not exist, please try again.");
						continue;
					}
				} else if (userInput.startsWith("delete song")) {
					String[] userInputSplited = userInput.split(" ");
					int songIndex;
					System.out
							.println("Are you sure you want to permanently remove this song?(yes to confirm, type anything to return to menu)");
					String confirm = br.readLine().trim();
					// additional layer of confirmation, in case of accidental
					// deletion
					if (confirm.equals("yes")) {
						try {
							songIndex = Integer.parseInt(userInputSplited[2]) - 1;
						} catch (NumberFormatException nfe) {
							System.out.println("Please enter a song index!");
							continue;
						}
						try {
							library.delSong(songIndex);
							library = Execution.readPlaylistXml(library);
							library.displayAllLibrarySongs();
							library.displayAllLibraryPlaylists();
						}

						catch (IndexOutOfBoundsException iobe) {
							System.out
									.println("Song does not exist, please try again.");
							continue;
						}
					}
				}

				else if (userInput.startsWith("play random")) {
					// User may enter any of the three commands that begin with
					// play random
					// each is encased in an if block
					List<Integer> indexes;
					if (userInput.equals("play random for all")) {
						int numberOfSongs = library.numberOfSongs();

						indexes = new ArrayList<Integer>();
						for (int i = 0; i < numberOfSongs; i++) {
							indexes.add(i);
						}
						player = Execution.playRandom(library, player, indexes);

					} else if (userInput.startsWith("play random")
							& userInput.endsWith(")")) {
						// When user wants to play specified songs randomly
						String[] userInputSplited = userInput.split(" ");
						userInputSplited = userInputSplited[2].substring(1,
								userInputSplited[2].length() - 1).split(",");
						ArrayList<String> tempList = new ArrayList<String>(
								Arrays.asList(userInputSplited));

						indexes = new ArrayList<Integer>(tempList.size());
						for (String i : tempList) {
							if (Integer.valueOf(i) > library.numberOfSongs()) {
								System.out
										.println("the song of index "
												+ Integer.valueOf(i)
												+ " does not exist in your music libaray.");
							} else {
								indexes.add(Integer.valueOf(i) - 1);

							}
						}
						player = Execution.playRandom(library, player, indexes);

					} else if (userInput.startsWith("play random playlist")) {
						String[] userInputSplited = userInput.split(" ");
						// The 4th element in list is the playlist that user
						// wants to play randomly
						String playlist = userInputSplited[3];
						Playlist pl = library.findPlaylist(playlist);
						try {
							indexes = new ArrayList<Integer>(pl.numberOfSongs());
						} catch (NullPointerException npe) {
							System.out.println("Playlist " + playlist
									+ " does not exist. Please try again.");
							continue;
						}

						for (int n = 0; n < pl.numberOfSongs(); n++) {
							indexes.add(n);
						}
						player = Execution.playRandom(library, player, pl,
								indexes);
					}

				} else if (userInput.startsWith("download")) {
					String title = userInput.split("download ")[1];
					library.downloadSong(title);

				} else if (userInput.startsWith("display jcloud songs")) {
					library.displayJcloudSongs();

				} else if (userInput.startsWith("get downloaded songs")) {
					library.downloadPreviousSongs();
					library.displayAllLibrarySongs();
				}

				else if (userInput.equals("display songs")) {
					library.displayAllLibrarySongs();
				} else if (userInput.equals("display library")) {
					library.displayAllLibrarySongs();
					library.displayAllLibraryPlaylists();
				}

				else if (userInput.equals("display playlists")) {
					library.displayAllLibraryPlaylists();
					// Shows nothing when no playlist have been created
				} else if (userInput.equals("help")) {
					displayUserManual();
				} else if (userInput.contains("pause")) {
					try {
						player.pause();
					} catch (NullPointerException e) {
						continue;
					}
				} else if (userInput.contains("resume")) {
					try {
						player.resume();
					} catch (NullPointerException e) {
						continue;
					}
				} else {
					System.out
							.println("Invalid command. Please pay attention to input format and try again!");
				}
			} catch (IOException e) {

				e.printStackTrace();
			}
		}
	}

	/**
	 * Display welcome message and jTunes's current version.
	 * 
	 */
	public static void displayWelcomeMessage() {
		System.out.println();
		System.out.println("Welcome to Jtunes 1.1!");
		System.out.println();
	}

	/**
	 * Displays the user manual
	 * 
	 */
	public static void displayUserManual() {
		System.out
				.println("*******************************User Manual*****************************************************************************************************************");
		System.out
				.println("play song 1 ---- play the first song from the library.");
		System.out
				.println("delete song 1 ---- delete the first song from the library.");
		System.out
				.println("play playlist java ---- play the songs in playlist user created in order.");
		System.out
				.println("play random for all --- play every song from main library one by one randomly.");
		System.out
				.println("play random (1,2,3)(no space in bracket) --- play first three songs from main library randomly.");
		System.out
				.println("create playlist java (1,2,3,4)(no space in bracket, no duplicates)--- create a playlist name java which contains first 4 songs in the main library.");
		System.out
				.println("play playlist java 2 --- play the second song from playlist java");
		System.out.println("delete playlist java --- delete playlist java");
		System.out
				.println("find songs by john --- create a playlist of all songs by artist john which can be played like a playlist.");
		System.out
				.println("play random playlist java --- play songs from playlist java one by one randomly");

		System.out
				.println("download This Is It --- download the song This Is It from jTunes web service (case sensitive)");

		System.out
				.println("display jcloud songs --- displays all songs available in JCloud");
		System.out
				.println("get downloaded songs --- downloads from JCloud all the songs you previous downloaded into your current directory");

		System.out
				.println("display songs --- displays all current songs in your library");

		System.out
				.println("display playlists --- displays all playlists created in library");
		System.out
				.println("display library --- displays all songs and playlists in library");
		System.out.println("quit --- quit jTunes");
		System.out.println("help --- display user manual");
		System.out.println("pause --- pause the song that's playing");
		System.out.println("resume --- resume a paused song");
		System.out
				.println("*******************************User Manual*****************************************************************************************************************");

	}
}
