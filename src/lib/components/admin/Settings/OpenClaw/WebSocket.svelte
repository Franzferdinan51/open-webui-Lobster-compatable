<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  
  export let gatewayUrl = 'http://100.106.80.61:18789';
  
  let socket: WebSocket | null = null;
  let connected = false;
  let messages: any[] = [];
  let status = 'disconnected';
  
  function connect() {
    status = 'connecting';
    try {
      const wsUrl = gatewayUrl.replace('http', 'ws') + '/ws';
      socket = new WebSocket(wsUrl);
      
      socket.onopen = () => {
        connected = true;
        status = 'connected';
        messages = [...messages, { type: 'system', content: 'Connected to gateway' }];
      };
      
      socket.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          messages = [...messages, { type: 'receive', content: data, time: new Date().toLocaleTimeString() }];
        } catch {
          messages = [...messages, { type: 'receive', content: event.data, time: new Date().toLocaleTimeString() }];
        }
      };
      
      socket.onclose = () => {
        connected = false;
        status = 'disconnected';
        messages = [...messages, { type: 'system', content: 'Disconnected from gateway' }];
      };
      
      socket.onerror = () => {
        status = 'error';
        messages = [...messages, { type: 'system', content: 'Connection error' }];
      };
    } catch (e) {
      status = 'error';
      messages = [...messages, { type: 'system', content: 'Failed to connect' }];
    }
  }
  
  function disconnect() {
    if (socket) {
      socket.close();
      socket = null;
    }
  }
  
  function sendMessage(content: string) {
    if (socket && connected) {
      socket.send(content);
      messages = [...messages, { type: 'send', content, time: new Date().toLocaleTimeString() }];
    }
  }
  
  let messageInput = '';
  
  function handleSend() {
    if (messageInput.trim()) {
      sendMessage(messageInput);
      messageInput = '';
    }
  }
  
  onDestroy(() => {
    disconnect();
  });
</script>

<div class="websocket-panel">
  <div class="flex items-center justify-between mb-4">
    <h2 class="text-2xl font-bold">🔌 WebSocket Client</h2>
    <div class="flex items-center gap-2">
      <span class="px-2 py-1 text-xs rounded-full {connected ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}">
        {status}
      </span>
      {#if connected}
        <button on:click={disconnect} class="px-3 py-1 bg-red-600 text-white rounded text-sm">
          Disconnect
        </button>
      {:else}
        <button on:click={connect} class="px-3 py-1 bg-blue-600 text-white rounded text-sm">
          Connect
        </button>
      {/if}
    </div>
  </div>
  
  <div class="mb-2">
    <label class="text-sm font-medium">Gateway URL</label>
    <input 
      bind:value={gatewayUrl}
      type="text" 
      class="w-full px-3 py-2 border rounded-lg bg-white dark:bg-gray-800"
      placeholder="http://100.106.80.61:18789"
    />
  </div>
  
  <!-- Messages -->
  <div class="bg-gray-100 dark:bg-gray-900 rounded-lg p-3 h-64 overflow-y-auto mb-3">
    {#each messages as msg}
      <div class="mb-1 text-sm {msg.type === 'system' ? 'text-yellow-500' : msg.type === 'send' ? 'text-blue-500' : 'text-green-500'}">
        <span class="text-xs text-gray-500">[{msg.time}]</span>
        <span class="font-medium">{msg.type === 'send' ? '→' : msg.type === 'receive' ? '←' : '•'}</span>
        {typeof msg.content === 'object' ? JSON.stringify(msg.content) : msg.content}
      </div>
    {/each}
    {#if messages.length === 0}
      <p class="text-gray-500 text-sm">No messages yet. Connect to start.</p>
    {/if}
  </div>
  
  <!-- Input -->
  <div class="flex gap-2">
    <input 
      bind:value={messageInput}
      type="text" 
      class="flex-1 px-3 py-2 border rounded-lg bg-white dark:bg-gray-800"
      placeholder="Enter message..."
      on:keydown={(e) => e.key === 'Enter' && handleSend()}
    />
    <button 
      on:click={handleSend}
      disabled={!connected}
      class="px-4 py-2 bg-blue-600 text-white rounded-lg disabled:opacity-50"
    >
      Send
    </button>
  </div>
</div>
