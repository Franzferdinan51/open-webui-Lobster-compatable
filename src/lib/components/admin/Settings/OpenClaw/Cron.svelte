<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  
  export let jobs: any[] = [];
  export let loading = false;
  
  let showAddModal = false;
  let newJob = { name: '', schedule: 'hourly', command: '' };
  
  const dispatch = createEventDispatcher();
  
  function getStatusColor(status: string) {
    switch (status) {
      case 'running': return 'bg-green-500';
      case 'error': return 'bg-red-500';
      case 'idle': return 'bg-gray-400';
      default: return 'bg-gray-400';
    }
  }
  
  async function addJob() {
    // Dispatch event to parent to handle API call
    dispatch('addJob', newJob);
    showAddModal = false;
    newJob = { name: '', schedule: 'hourly', command: '' };
  }
</script>

<div class="cron-panel">
  <div class="flex items-center justify-between mb-6">
    <h2 class="text-2xl font-bold">⏰ Cron Jobs</h2>
    <button 
      on:click={() => showAddModal = true}
      class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
    >
      + Add Job
    </button>
  </div>
  
  {#if showAddModal}
    <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 w-full max-w-md shadow-xl">
        <h3 class="text-xl font-bold mb-4">Add Cron Job</h3>
        
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium mb-1">Job Name</label>
            <input 
              bind:value={newJob.name}
              type="text" 
              class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700"
              placeholder="My Cron Job"
            />
          </div>
          
          <div>
            <label class="block text-sm font-medium mb-1">Schedule</label>
            <select 
              bind:value={newJob.schedule}
              class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700"
            >
              <option value="every-minute">Every Minute</option>
              <option value="every-5-minutes">Every 5 Minutes</option>
              <option value="every-15-minutes">Every 15 Minutes</option>
              <option value="every-30-minutes">Every 30 Minutes</option>
              <option value="hourly">Hourly</option>
              <option value="daily">Daily</option>
              <option value="weekly">Weekly</option>
            </select>
          </div>
          
          <div>
            <label class="block text-sm font-medium mb-1">Command</label>
            <textarea 
              bind:value={newJob.command}
              class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 font-mono text-sm"
              placeholder="echo 'Hello World'"
              rows="3"
            ></textarea>
          </div>
        </div>
        
        <div class="flex justify-end gap-2 mt-6">
          <button 
            on:click={() => showAddModal = false}
            class="px-4 py-2 bg-gray-200 dark:bg-gray-700 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600"
          >
            Cancel
          </button>
          <button 
            on:click={addJob}
            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            Add Job
          </button>
        </div>
      </div>
    </div>
  {/if}
  
  {#if loading}
    <div class="flex items-center justify-center py-12">
      <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
    </div>
  {:else}
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow overflow-hidden">
      <table class="w-full">
        <thead class="bg-gray-50 dark:bg-gray-900">
          <tr>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Name</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Schedule</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Status</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Last Run</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Next Run</th>
            <th class="px-4 py-3 text-right text-xs font-medium text-gray-500 uppercase">Actions</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
          {#each jobs as job}
            <tr>
              <td class="px-4 py-3 font-medium">{job.name}</td>
              <td class="px-4 py-3 text-sm font-mono">{job.schedule}</td>
              <td class="px-4 py-3">
                <span class={`inline-flex items-center gap-1 text-xs px-2 py-0.5 rounded-full ${getStatusColor(job.status)} text-white`}>
                  {job.status}
                </span>
              </td>
              <td class="px-4 py-3 text-sm text-gray-500">
                {job.last_run ? new Date(job.last_run).toLocaleString() : '—'}
              </td>
              <td class="px-4 py-3 text-sm text-gray-500">
                {job.next_run ? new Date(job.next_run).toLocaleString() : '—'}
              </td>
              <td class="px-4 py-3 text-right">
                <button class="px-2 py-1 text-sm bg-blue-100 dark:bg-blue-900/30 text-blue-700 rounded hover:bg-blue-200 mr-1">
                  Run
                </button>
                <button class="px-2 py-1 text-sm bg-gray-100 dark:bg-gray-700 rounded hover:bg-gray-200">
                  Edit
                </button>
              </td>
            </tr>
          {/each}
          
          {#if jobs.length === 0}
            <tr>
              <td colspan="6" class="px-4 py-12 text-center text-gray-500">
                No cron jobs configured
              </td>
            </tr>
          {/if}
        </tbody>
      </table>
    </div>
  {/if}
</div>

<style>
  .cron-panel {
    padding: 1rem;
  }
</style>
